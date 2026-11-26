# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `RPO_100`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_100/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 21 |
| Player Tracks | 21 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 57 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 92, Column 'Route': Unknown or unsupported route concept '-' in Route descriptor '-,23'.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [50-105] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [51-66] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [70-96] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-108] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-104] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-73] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-119] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-180] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [73-161] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-123] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-180] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-161] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-155] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-170] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-178] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-147] for track '20' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.