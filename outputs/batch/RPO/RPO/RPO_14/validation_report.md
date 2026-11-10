# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `RPO_14`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_14/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 69 |
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
> - Action 'Action_PreSnap' range [0-140] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-178] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-130] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-138] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-155] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-146] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-149] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-109] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-114] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-180] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-65] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-71] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-85] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-72] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-180] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-110] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-131] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-164] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-168] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-145] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-159] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-17] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-30] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-111] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-133] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-66] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-72] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-104] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-85] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-180] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-96] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-174] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-132] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-105] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-147] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-121] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-171] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-147] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-117] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-128] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-129] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-155] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-180] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-159] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-176] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-162] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '36' has 1 frames without a visible bounding box.
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
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.