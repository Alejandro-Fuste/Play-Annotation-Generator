# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_218`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_218/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 115 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [30-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-149] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-210] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-56] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-93] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-178] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-193] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-46] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [50-56] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-64] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-80] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-85] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-98] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-126] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-154] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [156-159] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-176] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-210] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-65] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-90] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-112] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-129] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-210] for track '6' has 8 frames without a visible bounding box.
> - Action 'Action_None' range [30-95] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-34] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-41] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [46-74] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [91-92] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-95] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-46] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [60-62] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-70] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-190] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-200] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-39] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-67] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-68] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [72-86] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-33] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [35-38] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [40-43] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-59] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-102] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-210] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-33] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-44] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-32] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-59] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [63-71] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-97] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [100-120] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-176] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-204] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-31] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-119] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-126] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-149] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-158] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-116] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-210] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-210] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [127-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-141] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [152-155] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-183] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-171] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-170] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-192] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-201] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-179] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '30' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.