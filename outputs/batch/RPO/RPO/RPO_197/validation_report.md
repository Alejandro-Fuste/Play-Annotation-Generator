# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `RPO_197`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_197/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 42 |
| Player Tracks | 42 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - RPO Run Block requires exactly five verified OL positions ['C', 'LG', 'LT', 'RG', 'RT']; found ['LG', 'LT', 'RG', 'RT'].

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-70] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-86] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-145] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-180] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-24] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-61] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-89] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-72] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-91] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullBall' range [11-12] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-139] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-145] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-157] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-42] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-52] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-116] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-136] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-131] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-135] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-132] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-130] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-136] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-139] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-142] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-149] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-157] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-161] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-166] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-170] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-180] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-153] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-157] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-174] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-180] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-168] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-168] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-180] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-180] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-177] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-178] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-180] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-176] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '41' has 1 frames without a visible bounding box.
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
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.