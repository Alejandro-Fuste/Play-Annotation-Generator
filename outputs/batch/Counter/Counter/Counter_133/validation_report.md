# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_133`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_133/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '12' (LT) duration 105 frames exceeds threshold 90 frames [start=162, end=266].
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [159–174], lower_priority='Action_DownBlock' annotated_start=162, effective_Action_DownBlock_start=175.
> - Validation warning: Action 'Action_DownBlock' for track '23' (LG) duration 105 frames exceeds threshold 90 frames [start=162, end=266].
> - Action 'Action_None' range [159-329] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [159-314] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-314] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-321] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-325] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-329] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-321] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-319] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-326] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '12' starts at frame 267, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [267-267] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-321] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [323-328] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-206] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-215] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-316] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-325] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-292] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-318] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [175-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [193-194] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [198-201] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [206-209] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [162-222] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-329] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-32] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-7] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-10] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-31] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-37] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [162-195] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [197-198] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-327] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [193-265] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [271-305] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [310-318] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-133] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-214] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-320] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [322-329] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-234] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-253] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-319] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-305] for track '30' has 1 frames without a visible bounding box.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
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