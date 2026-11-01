# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_134`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_134/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [89–102], lower_priority='Action_ZoneBlock' annotated_start=91, effective_Action_ZoneBlock_start=103.
> - Action 'Action_ZoneBlock' range [91-144] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-214] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-231] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-267] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [91-118] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-227] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-251] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-260] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-122] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-124] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [133-171] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [175-179] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [181-228] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [231-248] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [89-122] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-214] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-101] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [89-94] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [91-106] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [108-146] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-217] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-235] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [103-140] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-160] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-138] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-157] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-138] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-225] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-143] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-166] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-209] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-219] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-269] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-185] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-269] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-193] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-209] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-256] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-262] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-249] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-246] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-253] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-256] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-266] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [266-268] for track '28' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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