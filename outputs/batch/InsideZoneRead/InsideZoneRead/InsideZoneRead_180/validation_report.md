# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_180`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_180/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 86 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '12' (RT) duration 98 frames exceeds threshold 90 frames [start=101, end=198].
> - Validation warning: Action 'Action_ZoneBlock' for track '14' (LT) duration 98 frames exceeds threshold 90 frames [start=101, end=198].
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (C) duration 98 frames exceeds threshold 90 frames [start=101, end=198].
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [98–112], lower_priority='Action_ZoneBlock' annotated_start=101, effective_Action_ZoneBlock_start=113.
> - Action 'Action_None' range [98-198] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-241] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-245] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-271] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [141-243] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [245-270] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [273-289] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-142] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-157] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-299] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-299] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-299] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-166] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-192] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-299] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-179] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [185-198] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-262] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-125] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [127-129] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [146-147] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-273] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-248] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-120] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-13] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-36] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-50] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-94] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-180] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-299] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-227] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-247] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-257] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-266] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-276] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-286] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [293-296] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-274] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-299] for track '28' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.