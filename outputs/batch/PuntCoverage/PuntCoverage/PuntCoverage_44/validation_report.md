# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_44`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_44/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 94 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [5-87] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-178] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-182] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-110] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-129] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-135] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-143] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-299] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [5-173] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-255] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [257-289] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-32] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-84] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-135] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-152] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-145] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [148-151] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-179] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [5-114] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-122] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-134] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-125] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-168] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-299] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-128] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-226] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-30] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-145] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-279] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-192] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [61-299] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-65] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-299] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-152] for track '19' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [12-120] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-137] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-266] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-45] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [227-263] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-281] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [210-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [244-254] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [261-272] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [286-299] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-178] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-202] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-207] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-218] for track '28' has 1 frames without a visible bounding box.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.