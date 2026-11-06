# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_45`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_45/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 71 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 91: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - Row 92: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [21-83] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-127] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-149] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-195] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-74] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-178] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [21-68] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-54] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-71] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-88] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-259] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-45] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-106] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [243-280] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-68] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-286] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-299] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-79] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-299] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-133] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [219-292] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-240] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-243] for track '30' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.