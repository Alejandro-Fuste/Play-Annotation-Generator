# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_16`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_16/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 32 |
| Ball Tracks | 1 |
| CSV events parsed | 21 |
| Action Segments inferred | 79 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [171–187], lower_priority='Action_ZoneBlock' annotated_start=174, effective_Action_ZoneBlock_start=188.
> - Validation warning: Action 'Action_ZoneBlock' for track '11' (RT) duration 95 frames exceeds threshold 90 frames [start=174, end=268].
> - Validation warning: Action 'Action_ZoneBlock' for track '15' (LG) duration 95 frames exceeds threshold 90 frames [start=174, end=268].
> - Action 'Action_None' range [171-294] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-343] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-355] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [361-364] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-339] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [183-268] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-368] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-222] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [223-278] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-289] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-397] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-379] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-407] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-419] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [221-263] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [265-266] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-288] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [290-292] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-419] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-399] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [174-240] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-216] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-419] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [174-256] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-350] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [356-364] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-66] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-96] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-125] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-139] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-142] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-160] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-170] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-174] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-270] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-351] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-361] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-308] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [243-244] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-272] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-286] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [284-288] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-299] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-302] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-349] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-345] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [325-338] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-417] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-419] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-382] for track '30' has 1 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.