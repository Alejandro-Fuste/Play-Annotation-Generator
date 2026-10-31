# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Hitch_52`
- **Input XML**: `outputs/batch/Hitch/Hitch/Hitch_52/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Hitch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 64 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [20–37], lower_priority='Action_PassBlock' annotated_start=23, effective_Action_PassBlock_start=38.
> - Action 'Action_RunHitchRoute' range [37-77] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunHitchRoute' range [82-84] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-235] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-61] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-46] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-214] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [23-58] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [38-115] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [122-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-177] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [23-205] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [208-209] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [23-69] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [73-74] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-86] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-239] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-221] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-229] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '25' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.