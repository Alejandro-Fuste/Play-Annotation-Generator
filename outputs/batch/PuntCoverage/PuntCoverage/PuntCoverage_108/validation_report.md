# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_108`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_108/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 63 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Segment 'Action_Tackle' for track '34' has invalid range: start=316, end=297. Clamping end to start.
> - Action 'Action_PreSnap' range [0-159] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-329] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-282] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-291] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-304] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-147] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-159] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-259] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-144] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-155] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-160] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-329] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-113] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-59] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-66] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-124] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-190] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-329] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-329] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-114] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-196] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-41] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-79] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-329] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-45] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-62] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-140] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-115] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-91] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-108] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-121] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-124] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [202-269] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-298] for track '32' has 1 frames without a visible bounding box.
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
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.