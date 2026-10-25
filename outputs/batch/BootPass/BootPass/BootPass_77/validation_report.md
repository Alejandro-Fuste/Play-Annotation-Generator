# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_77`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_77/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
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
> - Action 'Action_None' range [167-209] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-48] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-237] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [25-47] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [25-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-72] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-174] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [25-50] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '23' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.