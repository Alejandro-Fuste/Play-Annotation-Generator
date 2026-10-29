# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_94`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_94/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 60 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 418 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 190: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 418 as fallback play end.
> - Action 'Action_PreSnap' range [0-351] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [353-418] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-381] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [386-418] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-352] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [300-340] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-355] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-322] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-383] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-408] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-318] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-361] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-344] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-418] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-350] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [353-370] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [378-379] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [386-387] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [394-395] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-328] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-331] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [300-304] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [316-317] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-207] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-313] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-316] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-323] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-332] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-317] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-166] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-174] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-19] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-76] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-102] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-299] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [300-303] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-299] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-300] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [354-362] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [369-394] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-365] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-358] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [361-362] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [375-418] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [389-394] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [400-413] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [413-417] for track '29' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.