# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_163`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_163/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 53 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ComboBlock' for track '16' has invalid range: start=152, end=140. Clamping end to start.
> - Action 'Action_PreSnap' range [0-239] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-228] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-163] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-238] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-159] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-163] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-177] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-158] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-197] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-185] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-199] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-206] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-169] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-177] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-222] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [152-182] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-140] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-179] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [152-164] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [166-201] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [202-205] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [152-164] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [175-198] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-238] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-178] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-239] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-193] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-201] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-206] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-226] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-239] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-218] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-239] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-239] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-239] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-231] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-239] for track '30' has 2 frames without a visible bounding box.
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
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.