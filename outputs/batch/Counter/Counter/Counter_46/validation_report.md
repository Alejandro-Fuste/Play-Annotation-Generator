# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_46`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_46/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [183–197], lower_priority='Action_DownBlock' annotated_start=186, effective_Action_DownBlock_start=198.
> - Action 'Action_None' range [183-299] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-204] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-248] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-221] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-228] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-296] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [186-219] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-253] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-212] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-226] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-259] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-208] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [186-216] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [183-197] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_Handoff' range [205-206] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [211-219] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-290] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-182] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [198-201] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [204-213] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-43] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [186-228] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [245-246] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-52] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-57] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-68] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-73] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-117] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-121] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-127] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-131] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-185] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [186-198] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [237-238] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-283] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-288] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-224] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-212] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-202] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-212] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [223-280] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-251] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '18' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.