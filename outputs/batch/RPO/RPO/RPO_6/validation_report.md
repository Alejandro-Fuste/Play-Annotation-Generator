# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_6`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_6/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [77-104] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-111] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-159] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [164-171] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-210] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-122] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-159] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-168] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-146] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-174] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-89] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-184] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-203] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-106] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [114-143] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-153] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-164] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-172] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-87] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [92-141] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-149] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-98] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-115] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-194] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-162] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-191] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-140] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-131] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-162] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-113] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [119-123] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-25] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-147] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-59] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-68] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-131] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-156] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-169] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-170] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-183] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-174] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-195] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [202-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-178] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-190] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-203] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-210] for track '22' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.