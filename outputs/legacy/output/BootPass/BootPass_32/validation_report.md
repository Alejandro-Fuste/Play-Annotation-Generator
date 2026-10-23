# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_32`
- **Input XML**: `output/BootPass/BootPass_32/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 0 |
| Action Segments inferred | 50 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-180] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-108] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-87] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-55] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-62] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-54] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-109] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-91] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-58] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-92] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-34] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-71] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-88] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-93] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-97] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-105] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-89] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-180] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-98] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-120] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-155] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-162] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-168] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-178] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-157] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-153] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-159] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-174] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-179] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-172] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-179] for track '29' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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
> - Play definition: no definition found for 'Play_Unknown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.