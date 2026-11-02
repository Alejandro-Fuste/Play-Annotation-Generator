# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_233`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_233/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
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
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [62–83], lower_priority='Action_ZoneBlock' annotated_start=64, effective_Action_ZoneBlock_start=84.
> - Action 'Action_BallCarry' range [94-163] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-116] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-201] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-93] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-161] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [163-225] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-181] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-163] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-214] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-227] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-233] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-222] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [62-146] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-157] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-179] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-225] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-148] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-183] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-222] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-134] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-153] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-187] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [64-78] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [81-99] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [64-86] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-78] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-103] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-131] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-144] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-199] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-185] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-215] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-219] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-235] for track '29' has 2 frames without a visible bounding box.
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