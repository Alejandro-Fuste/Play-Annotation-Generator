# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_89`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_89/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 424 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 179: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - Row 180: Duplicate assignment for track ID '21' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 424 as fallback play end.
> - Action 'Action_PreSnap' range [0-80] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-87] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [282-328] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [330-366] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [370-371] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [376-378] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [380-400] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [403-407] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [412-413] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-273] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-279] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-291] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [320-358] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-311] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-374] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [411-412] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-249] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-353] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-371] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [373-374] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-377] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-424] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-383] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-343] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-424] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-77] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-80] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-249] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-307] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [309-312] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-320] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [253-277] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [280-281] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [253-302] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [308-310] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [315-323] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-415] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-249] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-274] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-424] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-77] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-338] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [342-343] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-300] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-304] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-306] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-416] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-309] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [318-320] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-420] for track '26' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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