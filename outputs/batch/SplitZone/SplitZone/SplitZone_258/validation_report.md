# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_258`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_258/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 28 |
| Ball Tracks | 3 |
| CSV events parsed | 22 |
| Action Segments inferred | 63 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '7' (LT) duration 107 frames exceeds threshold 90 frames [start=196, end=302].
> - Validation warning: Action 'Action_ZoneBlock' for track '8' (RG) duration 112 frames exceeds threshold 90 frames [start=196, end=307].
> - Validation warning: Action 'Action_ZoneBlock' for track '11' (LG) duration 112 frames exceeds threshold 90 frames [start=196, end=307].
> - Validation warning: Action 'Action_ZoneBlock' for track '15' (C) duration 112 frames exceeds threshold 90 frames [start=196, end=307].
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [193–200], lower_priority='Action_ZoneBlock' annotated_start=196, effective_Action_ZoneBlock_start=201.
> - Action 'Action_None' range [193-320] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-317] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-323] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-297] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-314] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-364] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-271] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [196-302] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-342] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-360] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-208] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [209-231] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [234-248] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [257-293] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-325] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-111] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-134] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [193-196] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-284] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-386] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [229-245] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [248-279] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [281-309] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [311-312] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [201-307] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [308-322] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-192] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-219] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-282] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-316] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [325-372] for track '26' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.