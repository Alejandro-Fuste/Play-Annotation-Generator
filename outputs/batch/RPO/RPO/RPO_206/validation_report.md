# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_206`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_206/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 21 |
| Player Tracks | 21 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
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
> - Action 'Action_None' range [45-108] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-100] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-116] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-150] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [101-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-146] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-110] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [46-48] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-144] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-110] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-67] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-79] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-52] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-89] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-72] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-83] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-150] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [76-139] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-141] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-150] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-150] for track '20' has 2 frames without a visible bounding box.
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
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.