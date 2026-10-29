# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_136`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_136/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 32 |
| Ball Tracks | 1 |
| CSV events parsed | 14 |
| Action Segments inferred | 57 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-199] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-239] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-159] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [170-185] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [199-201] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-234] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-181] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-79] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-119] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-124] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-169] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-190] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-37] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-53] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-56] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-59] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-66] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-73] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-40] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-239] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-138] for track '21' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-144] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-233] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-164] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-179] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-184] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-189] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-186] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-207] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-239] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-239] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-239] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-239] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-237] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-239] for track '32' has 1 frames without a visible bounding box.
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