# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Slants0to10_41`
- **Input XML**: `outputs/batch/Slants0to10/Slants0to10/Slants0to10_41/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Slants0to10.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 94 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [1–16], lower_priority='Action_PassBlock' annotated_start=4, effective_Action_PassBlock_start=17.
> - Action 'Action_None' range [1-299] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-249] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [251-267] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-277] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-284] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-50] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-56] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-64] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-78] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-81] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-167] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-68] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-40] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-105] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-39] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-257] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-28] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-66] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [71-257] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [17-25] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [27-122] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [124-128] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [131-267] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-237] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-80] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-89] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-95] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-131] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-284] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-71] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-279] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-13] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-17] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-103] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [106-113] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [115-279] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-255] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-106] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-249] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [260-265] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-136] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-143] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-202] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-273] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-243] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [249-265] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-135] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-250] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-196] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-228] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-224] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-264] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-292] for track '34' has 1 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_Pass_Slants0to10'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.