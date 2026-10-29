# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_178`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_178/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 32 |
| Ball Tracks | 1 |
| CSV events parsed | 14 |
| Action Segments inferred | 66 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-6] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-95] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-198] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-202] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-208] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-151] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [152-193] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [197-201] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-220] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [152-181] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-230] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-3] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-161] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-182] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-197] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-204] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-209] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-214] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [152-191] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-237] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-158] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-164] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-239] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-174] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-178] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-200] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-225] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-88] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-239] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-218] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-229] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-195] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-213] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-221] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-200] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-211] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-222] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-226] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-239] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-224] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-234] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-237] for track '32' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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