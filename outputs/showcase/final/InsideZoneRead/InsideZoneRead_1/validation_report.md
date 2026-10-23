# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_1`
- **Input XML**: `output_showcase_final/InsideZoneRead/InsideZoneRead_1/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [74–89], lower_priority='Action_ZoneBlock' annotated_start=76, effective_Action_ZoneBlock_start=90.
> - Action 'Action_None' range [74-227] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [76-135] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-132] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-198] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-206] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-232] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [76-115] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [119-128] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-219] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [159-163] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-160] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-104] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-134] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-131] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-176] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-195] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [76-96] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [99-105] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [107-146] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-235] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-109] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-125] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-232] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-228] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-183] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [190-228] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-18] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-32] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-61] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-127] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-168] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-184] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [186-199] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-238] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [152-159] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-230] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-218] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-224] for track '30' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.