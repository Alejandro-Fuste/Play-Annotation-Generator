# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_135`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_135/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [37-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-180] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [37-90] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-80] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-85] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [90-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [38-75] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-104] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-180] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [37-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-162] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-53] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-86] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-100] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [39-46] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [42-49] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [54-56] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [60-68] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-68] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-90] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-108] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-161] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-172] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-179] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-170] for track '30' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.