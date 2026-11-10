# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_199`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_199/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [49-131] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-144] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-142] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-168] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-180] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-168] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-74] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-161] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-175] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-87] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-180] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [50-113] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [49-175] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-112] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-105] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-142] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-84] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-123] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-180] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [50-59] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [61-63] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [65-67] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-101] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [50-67] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [73-76] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [50-71] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [73-90] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [96-102] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [105-107] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-178] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-161] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-173] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-180] for track '24' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.