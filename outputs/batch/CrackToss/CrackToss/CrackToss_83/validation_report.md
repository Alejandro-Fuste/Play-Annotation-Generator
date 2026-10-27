# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_83`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_83/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 88 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 399 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 168: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - Row 168: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - Row 168: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 399 as fallback play end.
> - Action 'Action_None' range [269-372] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [377-386] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [389-395] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-399] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-371] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-364] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-369] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [272-305] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [347-399] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-276] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-399] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-375] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-286] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-327] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-335] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-373] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-329] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [332-333] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-339] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [272-341] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-369] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [394-395] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-280] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-373] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-399] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-376] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-337] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [342-346] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [349-374] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [377-379] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-385] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-397] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [298-299] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [298-308] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-372] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [389-390] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-313] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-347] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-352] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-373] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [392-395] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-377] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-392] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [387-399] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [395-396] for track '26' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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