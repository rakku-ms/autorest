// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root for
// license information.
// 
// Code generated by Microsoft (R) AutoRest Code Generator.
// Changes may cause incorrect behavior and will be lost if the code is
// regenerated.

namespace Fixtures.MirrorPolymorphic.Models
{
    using System.Linq;

    public partial class SiameseCat : BaseCat
    {
        /// <summary>
        /// Initializes a new instance of the SiameseCat class.
        /// </summary>
        public SiameseCat() { }

        /// <summary>
        /// Initializes a new instance of the SiameseCat class.
        /// </summary>
        /// <param name="id">Id.</param>
        /// <param name="description">Description of a Animal.</param>
        /// <param name="color">cat color</param>
        /// <param name="length">cat length</param>
        public SiameseCat(string id = default(string), string description = default(string), string color = default(string), int? length = default(int?))
            : base(id, description, color)
        {
            Length = length;
        }

        /// <summary>
        /// Gets or sets cat length
        /// </summary>
        [Newtonsoft.Json.JsonProperty(PropertyName = "length")]
        public int? Length { get; set; }

    }
}