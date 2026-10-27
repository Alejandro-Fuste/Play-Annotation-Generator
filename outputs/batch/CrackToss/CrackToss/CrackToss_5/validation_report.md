# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_5`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_5/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 90 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 358 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 12: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 12: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 358 as fallback play end.
> - Action 'Action_None' range [199-268] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-324] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [239-310] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-317] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-351] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-308] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-307] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-320] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-340] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-201] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [202-222] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-101] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-241] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [244-317] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-342] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-358] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-198] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-316] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-8] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-316] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-270] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-13] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [202-237] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [239-251] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-269] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-244] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-198] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-319] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-319] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-233] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [239-317] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-301] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-317] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-322] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-342] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [251-300] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-337] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-347] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-342] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-358] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-358] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-358] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-358] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-356] for track '31' has 2 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.