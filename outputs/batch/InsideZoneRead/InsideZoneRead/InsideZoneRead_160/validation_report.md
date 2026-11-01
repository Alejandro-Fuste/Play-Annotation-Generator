# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_160`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_160/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [131–145], lower_priority='Action_ZoneBlock' annotated_start=134, effective_Action_ZoneBlock_start=146.
> - Action 'Action_None' range [131-305] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-264] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-310] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-274] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-281] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-284] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [134-194] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-163] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-241] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [245-329] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [214-316] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [134-149] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [159-191] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [134-156] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [160-167] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [171-173] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-301] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-253] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-263] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-306] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-213] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [219-222] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-329] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [174-199] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [202-275] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [131-329] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-33] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-147] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-155] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-166] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-198] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-222] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-329] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-236] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-294] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-319] for track '30' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.