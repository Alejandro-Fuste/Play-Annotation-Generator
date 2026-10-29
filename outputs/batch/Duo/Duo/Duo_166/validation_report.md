# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_166`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_166/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 25 |
| Ball Tracks | 1 |
| CSV events parsed | 16 |
| Action Segments inferred | 48 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-152] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-167] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-140] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-157] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-171] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [96-135] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [138-139] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-164] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-169] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-135] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-200] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-209] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-106] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-111] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-115] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-147] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-147] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [96-98] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [114-115] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [132-141] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-159] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '14' has 9 frames without a visible bounding box.
> - Action 'Action_None' range [142-186] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-55] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-104] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-133] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-174] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-85] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-161] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-182] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-202] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-200] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-214] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-239] for track '25' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.