# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_136`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_136/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 19 |
| Player Tracks | 19 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 54 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [44-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [45-51] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [53-108] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-180] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-134] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-147] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-166] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-170] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-174] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-180] for track '18' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.