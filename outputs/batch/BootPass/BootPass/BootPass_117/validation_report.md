# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_117`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_117/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Overlapping action conflict at frame 19 for track '15': 'Action_RunBlock' vs 'Action_SnapReceive'. Overriding with 'Action_SnapReceive'.
> - Segment 'Action_SnapReceive' for track '15' has invalid range: start=41, end=19. Clamping end to start.
> - Segment 'Action_BallSnap' for track '16' has invalid range: start=41, end=19. Clamping end to start.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [41–41], lower_priority='Action_RunBlock' annotated_start=19, effective_Action_RunBlock_start=42.
> - Action 'Action_None' range [41-82] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-182] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [41-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-100] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-107] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-123] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-220] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-235] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-201] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [110-239] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [41-227] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-82] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-185] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [19-183] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-102] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-73] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-77] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [19-90] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [92-93] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [96-97] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [101-175] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [41-118] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [19-62] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [68-75] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [81-171] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [41-154] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-69] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-160] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-89] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-181] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-95] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-118] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-157] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-162] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-125] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-137] for track '27' has 1 frames without a visible bounding box.
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