# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_121`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_121/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 57 |
| Player Tracks | 57 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 167 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [67-206] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-125] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [67-102] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-172] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-252] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-113] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-155] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-179] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [190-192] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-201] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-269] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-93] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [131-223] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-177] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [68-78] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [80-128] for track '9' has 5 frames without a visible bounding box.
> - Action 'Action_None' for track '9' starts at frame 131, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [131-131] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-140] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-154] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-183] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-217] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-107] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-154] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-242] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [252-258] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [71-86] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-263] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-227] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [67-115] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-160] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-165] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-149] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-167] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-177] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-81] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-99] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [68-121] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-142] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-171] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [68-130] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-173] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-15] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-27] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-50] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-93] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-103] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-122] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-150] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [152-171] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-189] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-202] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [68-116] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [123-127] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-114] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [118-269] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-97] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-117] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-127] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-190] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-233] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [255-257] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-173] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-217] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-153] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-155] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-269] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-242] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-269] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-167] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-187] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-200] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-241] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [256-262] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-165] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-183] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-192] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-202] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-185] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-227] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [231-236] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-198] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-212] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-224] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-245] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-263] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-203] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-269] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-269] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-207] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-212] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-220] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-235] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-248] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-253] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-263] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [246-248] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-263] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-259] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-268] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-260] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-268] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-262] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-269] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-268] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-269] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '56' has 1 frames without a visible bounding box.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.
> - Player track '51' has undefined position. Will map to Position_Unknown.
> - Player track '51' has undefined team_side. Will map to Team_Unknown.
> - Player track '52' has undefined position. Will map to Position_Unknown.
> - Player track '52' has undefined team_side. Will map to Team_Unknown.
> - Player track '53' has undefined position. Will map to Position_Unknown.
> - Player track '53' has undefined team_side. Will map to Team_Unknown.
> - Player track '54' has undefined position. Will map to Position_Unknown.
> - Player track '54' has undefined team_side. Will map to Team_Unknown.
> - Player track '55' has undefined position. Will map to Position_Unknown.
> - Player track '55' has undefined team_side. Will map to Team_Unknown.
> - Player track '56' has undefined position. Will map to Position_Unknown.
> - Player track '56' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.