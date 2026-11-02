# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_109`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_109/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 60 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [39–57], lower_priority='Action_ZoneBlock' annotated_start=42, effective_Action_ZoneBlock_start=58.
> - Action 'Action_None' range [39-53] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-104] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-174] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [176-178] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-180] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [39-174] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [42-116] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-131] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [42-108] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-105] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [42-93] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-81] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-138] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-177] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [42-61] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [64-68] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [70-82] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-128] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-180] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [58-97] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-104] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-101] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-74] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-161] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [43-69] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [71-157] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-86] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-180] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-157] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-170] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-180] for track '24' has 3 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.