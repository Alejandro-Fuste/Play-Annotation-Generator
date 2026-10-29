# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_110`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_110/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 31 |
| Ball Tracks | 1 |
| CSV events parsed | 15 |
| Action Segments inferred | 63 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 268 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 268 as fallback play end.
> - Action 'Action_PreSnap' range [0-165] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-232] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-241] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-182] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-198] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-176] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-219] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-126] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-137] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-268] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-200] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-238] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-243] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-257] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-268] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [163-190] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [195-196] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [200-201] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [163-173] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [175-221] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [222-231] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-106] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-61] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-205] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-251] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-257] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-267] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-226] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-268] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-192] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-245] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-209] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-268] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-211] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-222] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-230] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-233] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-241] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-250] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-257] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-242] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-241] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-245] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-250] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-253] for track '31' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.