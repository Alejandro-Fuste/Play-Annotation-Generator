# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_155`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_155/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 88 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [58-181] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-112] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-145] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-178] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-91] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-103] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-156] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-191] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [58-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-119] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-138] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-148] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-166] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-170] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [59-78] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-166] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-134] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-165] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-188] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-225] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [59-61] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [88-97] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-125] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-136] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-155] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-170] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-61] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-71] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-86] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-159] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-219] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-128] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-136] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [59-65] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [91-104] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-173] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-187] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-75] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-152] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-59] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-64] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-82] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-140] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-146] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-223] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-83] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '23' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.