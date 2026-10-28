# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_50`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_50/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 69 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '15' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [51–65], lower_priority='Action_PassBlock' annotated_start=54, effective_Action_PassBlock_start=66.
> - Action 'Action_None' range [51-93] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-74] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [54-117] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-114] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [54-63] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [83-88] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-201] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-95] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-155] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-197] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-224] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_FakePassDroptoHandoff' range [71-95] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [107-111] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [54-74] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [90-101] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [111-116] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [124-146] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-70] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-74] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-148] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-133] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-229] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-238] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-185] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-194] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-204] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-231] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-204] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-234] for track '25' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.