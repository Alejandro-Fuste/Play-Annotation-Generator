# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_235`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_235/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 97 |
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
> - Action 'Action_PreSnap' range [0-149] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-223] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [132-164] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [180-182] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-219] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-223] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-234] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-221] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-227] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [132-192] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [194-195] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [198-201] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-151] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-239] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-220] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-239] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-126] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-220] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-64] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-117] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-158] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-194] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-216] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-233] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-199] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-143] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-151] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-157] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-179] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-185] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-200] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-205] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-146] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-31] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-39] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-121] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-156] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-192] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-200] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-219] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-24] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-27] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-34] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-41] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-49] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-54] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-57] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-82] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-91] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-115] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-127] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-112] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [132-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [182-183] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-128] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-131] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-139] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-143] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-156] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-176] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-161] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-139] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-155] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-170] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-200] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-204] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-213] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-208] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-239] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-218] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-226] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-239] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-234] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-224] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-226] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-233] for track '31' has 1 frames without a visible bounding box.
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
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.