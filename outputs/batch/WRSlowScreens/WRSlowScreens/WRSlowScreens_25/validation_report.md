# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `WRSlowScreens_25`
- **Input XML**: `outputs/batch/WRSlowScreens/WRSlowScreens/WRSlowScreens_25/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/WRSlowScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 65 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 9, Column 'Ball Snap': Unknown/missing frame number '' in entry ',19'.
> - Row 9, Column 'Pass Block': Unknown/missing frame number '' in entry ',OL'.
> - Row 9, Column 'Snap Receive': Unknown/missing frame number '' in entry ',15'.
> - Row 9, Column 'Release to Screen': Unknown/missing frame number '' in entry ',19'.
> - Row 9, Column 'Turn To Quarterback': Unknown/missing frame number '' in entry ',8'.
> - Row 9, Column 'Throw Screen Pass': Unknown/missing frame number '' in entry ',15'.
> - Row 9, Column 'Run After Catch': Unknown/missing frame number '' in entry ',8'.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [0-146] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-144] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-188] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-157] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-299] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-105] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-114] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-235] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-177] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-240] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-245] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-296] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-218] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-63] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-160] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-164] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-167] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-206] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-256] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-270] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-98] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-139] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-233] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-240] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-142] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-145] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-132] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-147] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-131] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-237] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-294] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-174] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-184] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-299] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-183] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-299] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-237] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-265] for track '32' has 1 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_Pass_WRSlowScreens'.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.