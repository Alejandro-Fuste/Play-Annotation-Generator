# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `RPO_113`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_113/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 59 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - RPO Run Block requires exactly five verified OL positions ['C', 'LG', 'LT', 'RG', 'RT']; found ['C', 'LT', 'RG', 'RT'].

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 208: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [0-225] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-158] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-173] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-183] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-197] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-218] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-253] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-258] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-222] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-229] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-240] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-231] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-262] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-268] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-219] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-204] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-131] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-140] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-147] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-162] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-172] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-184] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-223] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-194] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-262] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-238] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-95] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-107] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-261] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-124] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-178] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-188] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-194] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-181] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-194] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-213] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-237] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-237] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-243] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-247] for track '29' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
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
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.