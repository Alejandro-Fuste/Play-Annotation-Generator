# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_70`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_70/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 108 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '3' (LT) duration 95 frames exceeds threshold 90 frames [start=80, end=174].
> - Validation warning: Action 'Action_ZoneBlock' for track '5' (C) duration 95 frames exceeds threshold 90 frames [start=80, end=174].
> - Resolved action overlap for track '5' (C): higher_priority='Action_BallSnap' [74–89], lower_priority='Action_ZoneBlock' annotated_start=80, effective_Action_ZoneBlock_start=90.
> - Validation warning: Action 'Action_LeadBlock' for track '13' (RB) duration 95 frames exceeds threshold 90 frames [start=80, end=174].
> - Validation warning: Action 'Action_ZoneBlock' for track '14' (RG) duration 95 frames exceeds threshold 90 frames [start=80, end=174].
> - Validation warning: Action 'Action_ZoneBlock' for track '15' (LG) duration 95 frames exceeds threshold 90 frames [start=80, end=174].
> - Validation warning: Action 'Action_ZoneBlock' for track '16' (RT) duration 95 frames exceeds threshold 90 frames [start=80, end=174].
> - Action 'Action_BallCarry' range [106-228] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-151] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-167] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-196] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-243] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [245-248] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-263] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-276] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [74-266] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-271] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-289] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [90-131] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-272] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-279] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-132] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-143] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-152] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-172] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-193] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-292] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-299] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-299] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [80-118] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [121-123] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-275] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [277-281] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-287] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-298] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [80-85] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [95-174] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-191] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-248] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [250-273] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [80-131] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [133-142] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [144-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-278] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-240] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-250] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-257] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-263] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-219] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-258] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-281] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-293] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-191] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-201] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-299] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-92] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-104] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-133] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-219] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-222] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-291] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [293-299] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-277] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-286] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-279] for track '28' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.