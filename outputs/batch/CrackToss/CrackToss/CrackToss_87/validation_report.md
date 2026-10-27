# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `CrackToss_87`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_87/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 60 |
| Player Tracks | 58 |
| Ball Tracks | 2 |
| CSV events parsed | 15 |
| Action Segments inferred | 125 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 399 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_None' at frame 204 targets track ID '230', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 399 as fallback play end.
> - Action 'Action_PreSnap' range [0-145] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [164-201] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-215] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-151] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [155-175] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-273] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-319] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-231] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-315] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-315] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-160] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-205] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-309] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-187] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-203] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-235] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-185] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [184-194] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-151] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-190] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-177] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-285] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-315] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-345] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [351-396] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [398-399] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-240] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [242-250] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [252-300] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-162] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-151] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-233] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-244] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-39] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-142] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-315] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-17] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-36] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-41] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-56] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-61] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-68] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-139] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-151] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-190] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-262] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-173] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [166-200] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-315] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [178-259] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-216] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-229] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-315] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-260] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-295] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-347] for track '33' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [230-315] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-314] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-239] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [246-315] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-315] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-315] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [323-347] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-375] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-385] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [389-391] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-308] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-312] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-348] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [297-315] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-315] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-315] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-326] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-320] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-394] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [316-387] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-323] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-341] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-399] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-325] for track '52' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [316-322] for track '53' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [324-334] for track '53' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [316-317] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-372] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-376] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-387] for track '55' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [393-397] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-321] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-326] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-332] for track '56' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [317-322] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-325] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-340] for track '58' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '57' has undefined position. Will map to Position_Unknown.
> - Player track '57' has undefined team_side. Will map to Team_Unknown.
> - Player track '58' has undefined position. Will map to Position_Unknown.
> - Player track '58' has undefined team_side. Will map to Team_Unknown.
> - Player track '59' has undefined position. Will map to Position_Unknown.
> - Player track '59' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.