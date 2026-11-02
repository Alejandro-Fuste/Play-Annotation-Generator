# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_161`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_161/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [54-124] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-109] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-124] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-174] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [56-87] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-115] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-155] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-131] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [74-189] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [192-200] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [202-220] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [224-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-238] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-155] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-182] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-239] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-110] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-182] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-192] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-224] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-228] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-202] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-219] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-135] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-163] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-163] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-168] for track '33' has 1 frames without a visible bounding box.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.