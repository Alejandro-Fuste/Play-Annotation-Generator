# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `Sack_33`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_33/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 35, Column 'Sack Quarterback': Unknown actor track ID '?' in entry '265,?'.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [0-269] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-251] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-178] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-165] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-200] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-215] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-221] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-227] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-156] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-173] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-136] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-252] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-259] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-139] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-227] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-131] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-135] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-153] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-171] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-240] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-142] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-176] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-207] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-215] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-200] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-222] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-227] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-162] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [166-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [181-182] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-138] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-216] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-128] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-136] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-153] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-183] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-142] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-158] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-176] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-190] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-200] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-206] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-214] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-131] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-136] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-158] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-140] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-145] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-158] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-162] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-216] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-220] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-157] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-215] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-163] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-180] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-188] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-200] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-221] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-227] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-157] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-162] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-167] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-176] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-179] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-188] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-200] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-212] for track '29' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.