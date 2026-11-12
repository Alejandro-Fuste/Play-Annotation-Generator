# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_285`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_285/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [47–58], lower_priority='Action_ZoneBlock' annotated_start=55, effective_Action_ZoneBlock_start=59.
> - Action 'Action_None' range [47-182] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-252] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-116] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-101] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-115] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-179] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-190] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-204] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-106] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-232] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-253] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-104] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-189] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-91] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-155] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-76] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-240] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-261] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-108] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-92] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-229] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [87-264] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-94] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-130] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-151] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-167] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-254] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-269] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-205] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [207-214] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-211] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-259] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-217] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-224] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-234] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-269] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-246] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.