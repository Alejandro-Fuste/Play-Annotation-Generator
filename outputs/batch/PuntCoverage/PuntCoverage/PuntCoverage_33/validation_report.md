# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_33`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_33/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [4-185] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-64] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-69] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-176] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-226] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-216] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-112] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-126] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-123] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-239] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-105] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-108] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-125] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-54] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-57] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-61] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-86] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [89-92] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-173] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-217] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-100] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-113] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-121] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-71] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-105] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-109] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-224] for track '26' has 1 frames without a visible bounding box.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.