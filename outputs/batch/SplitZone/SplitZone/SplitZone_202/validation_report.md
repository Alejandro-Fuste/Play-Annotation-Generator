# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_202`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_202/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 96 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '8' (RT) duration 101 frames exceeds threshold 90 frames [start=146, end=246].
> - Segment 'Action_BallSnap' for track '9' has invalid range: start=143, end=65. Clamping end to start.
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (C) duration 139 frames exceeds threshold 90 frames [start=154, end=292].
> - Action 'Action_None' range [143-223] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-228] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-241] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-54] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-184] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-242] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-255] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [176-198] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [200-264] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-145] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [146-233] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-220] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-230] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [165-173] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-184] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [146-246] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-142] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-232] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-307] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [175-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [182-187] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [189-216] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [220-268] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [146-200] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [202-205] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-56] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-148] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-182] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-216] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-257] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-84] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-316] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-49] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-76] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-91] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-100] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-143] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [152-171] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [174-175] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [180-198] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [154-292] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-242] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-245] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-249] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-254] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-274] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-283] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-296] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-315] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-253] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-258] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-282] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-261] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-253] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-306] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [256-264] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-268] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-320] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-327] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-292] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-329] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-325] for track '32' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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