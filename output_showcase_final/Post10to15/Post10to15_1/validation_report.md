# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `Post10to15_1`
- **Input XML**: `output_showcase_final/Post10to15/Post10to15_1/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Post10to15.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_ThrowPass' at frame 59 targets track ID '64', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 3: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [4-41] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-100] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-150] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-68] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-150] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [4-38] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-150] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [4-150] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-150] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [22-150] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-53] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [21-98] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [104-125] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [127-131] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [134-137] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-14] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-17] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [28-39] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [49-51] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [54-56] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [60-61] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [66-80] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [87-88] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-77] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-18] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [40-84] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [87-129] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [131-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-28] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-150] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-59] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [87-93] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [97-150] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-82] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-150] for track '24' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.