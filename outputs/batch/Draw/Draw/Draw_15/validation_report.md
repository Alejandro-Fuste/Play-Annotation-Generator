# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_15`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_15/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 107 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [47–62], lower_priority='Action_PassBlock' annotated_start=50, effective_Action_PassBlock_start=63.
> - Action 'Action_None' range [47-117] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-128] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-219] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-227] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [50-94] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [97-126] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-138] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [104-113] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [115-246] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-254] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [259-265] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-86] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-94] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-112] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-118] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-134] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-269] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-117] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-125] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-116] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-124] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-94] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-114] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-124] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [127-130] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-268] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [63-149] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-163] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-94] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-130] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [50-103] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-39] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '22' starts at frame 47, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [47-47] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-52] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-62] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-74] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-121] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-269] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-171] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-209] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-242] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-183] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-197] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-213] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-234] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-250] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-269] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-191] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-208] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-221] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-263] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-259] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-266] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '32' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.