# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_381`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_381/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 116 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 761: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [8-99] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-106] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-210] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [90-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-61] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-210] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-45] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-80] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-99] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-154] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [8-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-43] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-54] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-59] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-71] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-107] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-153] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [8-107] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-145] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-210] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_Keep' range [38-45] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [49-51] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [58-59] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [63-210] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [11-45] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [58-59] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-152] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [8-44] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-59] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-71] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-100] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-106] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [11-45] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [54-89] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-181] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-185] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-45] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-59] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [61-74] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-80] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-106] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-210] for track '14' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [8-45] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-59] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-190] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-204] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-40] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-48] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [50-60] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-70] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-46] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-186] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [188-191] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-196] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [11-41] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [62-85] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-106] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [110-133] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [11-26] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [76-82] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-153] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-203] for track '20' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [205-209] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-44] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-74] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-86] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-117] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-84] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-92] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-191] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-154] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-185] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-192] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-202] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-154] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-210] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [160-165] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '29' has 1 frames without a visible bounding box.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_381'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.